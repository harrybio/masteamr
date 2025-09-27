import axios from 'axios';
import { API_BASE } from '../config';

export const getCountsSummary = () => axios.get(`${API_BASE}/summary/counts-summary`);
export const getTimeTrends = (period = 'month') => axios.get(`${API_BASE}/summary/time-trends?period=${period}`);
export const getOptions = () => axios.get(`${API_BASE}/options`);
