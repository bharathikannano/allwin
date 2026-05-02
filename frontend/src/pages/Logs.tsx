import { useEffect, useState } from 'react';
import { getTradeLogs } from '../services/api';

export default function Logs() {
  const [logs, setLogs] = useState<Record<string, any>[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await getTradeLogs();
        if (res.status === 'success') {
          setLogs(res.logs);
        }
      } catch (error) {
        console.error("Failed to fetch logs", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Trade Logs & Journal</h2>
      <div className="bg-slate-800 rounded-xl border border-slate-700 overflow-hidden">
        {loading ? (
           <div className="p-4 text-slate-400">Loading logs...</div>
        ) : (
          <table className="w-full text-left">
            <thead className="bg-slate-900 border-b border-slate-700">
              <tr>
                <th className="p-4 text-slate-400 font-medium">Symbol</th>
                <th className="p-4 text-slate-400 font-medium">Strategy</th>
                <th className="p-4 text-slate-400 font-medium">Entry Reason</th>
                <th className="p-4 text-slate-400 font-medium">Net PnL</th>
                <th className="p-4 text-slate-400 font-medium">Date</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-700">
              {logs.map((log) => (
                <tr key={log.id} className="hover:bg-slate-800/50">
                  <td className="p-4 font-medium">{log.symbol}</td>
                  <td className="p-4 text-slate-300">{log.strategy}</td>
                  <td className="p-4 text-slate-300">{log.entry_reason}</td>
                  <td className={`p-4 ${log.net_pnl >= 0 ? 'text-green-400' : 'text-red-400'}`}>
                    {log.net_pnl >= 0 ? '+' : '-'}₹{Math.abs(log.net_pnl).toFixed(2)}
                  </td>
                  <td className="p-4 text-slate-400">{new Date(log.entry_time).toLocaleDateString()}</td>
                </tr>
              ))}
              {logs.length === 0 && (
                 <tr>
                    <td colSpan={5} className="p-4 text-center text-slate-400">No logs found.</td>
                 </tr>
              )}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
