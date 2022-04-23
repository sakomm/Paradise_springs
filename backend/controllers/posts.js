import PostMessage from "../models/Listing.js";
import Safety from "../models/Safety.js"

export const getRecommendedPosts = async (req, res) => {
    try{    

    

            if(req.query.key !==undefined){
                //console.log("hi");
                //console.log(req.query.key)
               const Rating = await Safety.find({key:req.query.key})
               //console.log(Rating);
                res.status(200).json(Rating);
            }

            




            else if(req.query.state === "" && req.query.city === ""){
                
                const PostMessages = await PostMessage.aggregate([{$sample: {size:20}}])
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
            else if(req.query.city === ""){
                //make variables, check if they are defined, if they are pass them into the query statement

                const PostMessages = await PostMessage.aggregate([{$match: {$or: [
                    {state:req.query.state[0]},
                    {state:req.query.state[1]},
                    {state:req.query.state[2]}]
                    
                }},{$sample:{size:25}}]);
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
            else{
             
                const PostMessages = await PostMessage.aggregate([{$match: { $or: [
                    {city:req.query.city[0]},
                    {city:req.query.city[1]},
                    {city:req.query.city[2]}]
                    
                }},{$sample:{size:25}}]);
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
       
        

    }
    catch(error){
        
        res.status(404).json({message: error.message});
    }
}


export const createPost = async (req, res) => {
    const post = req.body;
    const newPost = new Listing(post);
    try{
        console.log('hello2');
        await newPost.save();
        res.status(201).json(newPost);
    }
    catch(error){
        res.status(409).json({message: error.message});
    }
}

export const getRatings = async (req, res) => {
    console.log("hello1");
    try{
        
        const SafteyRatings = await Saftey.find({key: "Florida"});
        console.log(Saftey);
        res.status(200).json(Saftey);

    }
    catch(error){
        
        res.status(404).json({message: error.message});
    }
}