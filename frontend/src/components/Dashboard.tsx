import React from 'react';
import NetworkVisualizer from './NetworkVisualizer';
import ResearchFeed from './ResearchFeed';
import ModelWorkspace from './ModelWorkspace';

const Dashboard: React.FC = () => {
  return (
    <div className="dashboard-container">
      <div className="left-panel">
        <NetworkVisualizer />
        <ModelWorkspace />
      </div>
      <div className="right-panel">
        <ResearchFeed />
      </div>
    </div>
  );
};

export default Dashboard;