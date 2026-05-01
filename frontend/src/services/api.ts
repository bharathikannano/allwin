import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const getDashboardSummary = async () => {
  const response = await axios.get(`${API_BASE_URL}/dashboard/`);
  return response.data;
};

export const getTradeLogs = async () => {
  const response = await axios.get(`${API_BASE_URL}/logs/`);
  return response.data;
};

export const runBacktest = async (data: any) => {
  const response = await axios.post(`${API_BASE_URL}/backtest/run`, data);
  return response.data;
};

export const getPaperPositions = async () => {
  const response = await axios.get(`${API_BASE_URL}/paper-trade/positions`);
  return response.data;
};

export const getLivePositions = async () => {
  const response = await axios.get(`${API_BASE_URL}/live-trade/positions`);
  return response.data;
};
