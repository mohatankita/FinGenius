import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import OptimizePortfolio from './pages/OptimizePortfolio';
import Performance from './pages/Performance';
import RiskHeatmap from './pages/RiskHeatmap';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/optimize" element={<OptimizePortfolio />} />
        <Route path="/performance" element={<Performance />} />
        <Route path="/heatmap" element={<RiskHeatmap />} />
      </Routes>
    </Router>
  );
}

export default App;
