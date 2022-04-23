import express from 'express'
import { getRecommendedPosts, createPost, getRatings} from '../controllers/posts.js'

const router = express.Router();

router.get('/', getRecommendedPosts);
router.get('/:state', getRatings);
router.post('/', createPost);



export default router;