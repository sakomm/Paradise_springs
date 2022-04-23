import mongoose from 'mongoose'

const postSchema = mongoose.Schema({
    state: [{type:String}],
    city: [{type:String}],
    guest: String
    
});
postSchema.set('collection', 'rentals_final');
const Listing = mongoose.model('Listing', postSchema, 'rentals_final');




export default Listing;