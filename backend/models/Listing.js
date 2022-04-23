import mongoose from 'mongoose'

const postSchema = mongoose.Schema({
    state: String,
    city: String,
    guests: String
    
});
postSchema.set('collection', 'rentals_final');
const Listing = mongoose.model('Listing', postSchema, 'rentals_final');




export default Listing;