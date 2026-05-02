import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { getDashboardSummary } from '../services/api';

const chartData = [
  { name: 'Mon', pnl: 4000 },
  { name: 'Tue', pnl: 3000 },
  { name: 'Wed', pnl: 2000 },
  { name: 'Thu', pnl: 2780 },
  { name: 'Fri', pnl: 1890 },
  { name: 'Sat', pnl: 2390 },
  { name: 'Sun', pnl: 3490 },
];

export default function Dashboard() {
  const [summary, setSummary] = useState<Record<string, any> | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await getDashboardSummary();
        if (res.status === 'success') {
          setSummary(res.data);
        }
      } catch (error) {
        console.error("Failed to fetch dashboard data", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold">Overview</h2>
        <p className="text-slate-400">Your trading performance at a glance.</p>
      </div>

      {loading ? (
        <div className="text-slate-400">Loading metrics...</div>
      ) : summary ? (
        <div className="grid grid-cols-4 gap-6">
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <h3 className="text-slate-400 text-sm font-medium">Net PnL</h3>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-2xl font-bold">₹{summary.total_pnl}</span>
            </div>
          </div>
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <h3 className="text-slate-400 text-sm font-medium">Win Rate</h3>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-2xl font-bold">{summary.win_rate}%</span>
            </div>
          </div>
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <h3 className="text-slate-400 text-sm font-medium">Active Positions</h3>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-2xl font-bold">{summary.active_positions}</span>
            </div>
          </div>
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
            <h3 className="text-slate-400 text-sm font-medium">Daily Drawdown</h3>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-2xl font-bold">{summary.daily_drawdown}%</span>
            </div>
          </div>
        </div>
      ) : (
        <div className="text-red-400">Failed to load data. Is the backend running?</div>
      )}

      {/* Chart */}
      <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 h-[400px]">
        <h3 className="text-lg font-medium mb-4">PnL Curve</h3>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="name" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip
              contentStyle={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}
              itemStyle={{ color: '#f8fafc' }}
            />
            <Line type="monotone" dataKey="pnl" stroke="#3b82f6" strokeWidth={2} dot={{ r: 4 }} activeDot={{ r: 6 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
