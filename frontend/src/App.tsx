
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { LayoutDashboard, TrendingUp, History, Activity, Database } from 'lucide-react';
import Dashboard from './pages/Dashboard';
import Backtest from './pages/Backtest';
import PaperTrade from './pages/PaperTrade';
import LiveTrade from './pages/LiveTrade';
import Logs from './pages/Logs';

function App() {
  return (
    <Router>
      <div className="flex h-screen bg-slate-900 text-slate-100 font-sans">
        {/* Sidebar */}
        <div className="w-64 bg-slate-800 border-r border-slate-700 p-4">
          <div className="flex items-center gap-2 mb-8 px-2">
            <Activity className="text-blue-500" />
            <h1 className="text-xl font-bold tracking-wider">TRADE<span className="text-blue-500">OS</span></h1>
          </div>
          <nav className="space-y-2">
            <Link to="/" className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-700 transition-colors">
              <LayoutDashboard size={20} className="text-slate-400" /> Dashboard
            </Link>
            <Link to="/backtest" className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-700 transition-colors">
              <History size={20} className="text-slate-400" /> Backtesting
            </Link>
            <Link to="/paper" className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-700 transition-colors">
              <Database size={20} className="text-slate-400" /> Paper Trading
            </Link>
            <Link to="/live" className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-700 transition-colors">
              <TrendingUp size={20} className="text-slate-400" /> Live Trading
            </Link>
            <Link to="/logs" className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-700 transition-colors">
              <Activity size={20} className="text-slate-400" /> Trade Logs
            </Link>
          </nav>
        </div>

        {/* Main Content */}
        <div className="flex-1 overflow-auto">
          <header className="h-16 border-b border-slate-800 flex items-center px-8 bg-slate-900/50 backdrop-blur-sm sticky top-0 z-10">
             <div className="flex-1"></div>
             <div className="flex items-center gap-4">
                <span className="text-sm font-medium px-3 py-1 bg-green-500/10 text-green-400 rounded-full border border-green-500/20">Market Open</span>
             </div>
          </header>
          <main className="p-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/backtest" element={<Backtest />} />
              <Route path="/paper" element={<PaperTrade />} />
              <Route path="/live" element={<LiveTrade />} />
              <Route path="/logs" element={<Logs />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
