import express from 'express'
import { getRecommendedPosts, createPost, getPosts} from '../controllers/posts.js'

const router = express.Router();

router.get('/', getRecommendedPosts);
router.get('/ResultsPage', getPosts);
router.post('/', createPost);



export default router;