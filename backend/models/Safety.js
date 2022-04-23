import mongoose from 'mongoose'

const safetySchema = mongoose.Schema({
    key: String,
    
    
});
safetySchema.set('collection', 'safety_stat');
const safety = mongoose.model('rating', safetySchema, 'safety_stat');




export default safety;