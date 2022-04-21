import axios from 'axios'

const url = 'http://localhost:3000/posts';
const url1 = 'http://localhost:3000/ResultsPage';
export const fetchPosts = (filters) => axios.get(url, filters);
export const fetchResults = (filters) => axios.get(url1, filters);


