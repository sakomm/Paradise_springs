import mongoose from 'mongoose'

const postSchema = mongoose.Schema({
    state: String,
    city: String,
    rental_amenities: Array,
    checkin: Date,
    checkout: Date
    
});
postSchema.set('collection', 'rentals_final');
const Listing = mongoose.model('Listing', postSchema, 'rentals_final');




export default Listing;