import axios from 'axios'

const url = 'http://localhost:5000/posts';
const url1 = 'http://localhost:5000/ResultsPage';
export const fetchPosts = (filters) => axios.get(url, filters);
export const fetchResults = (filters) => axios.get(url1, filters);
export const fetchRating =(filters) => axios.get(url,filters);

