import mongoose from 'mongoose'

const postSchema = mongoose.Schema({
    location: Array,
    checkin: String,
    checkout: String,
    guests: String,
});
postSchema.set('collection', 'rentals');
const Listing = mongoose.model('Listing', postSchema, 'rentals');





export default Listing