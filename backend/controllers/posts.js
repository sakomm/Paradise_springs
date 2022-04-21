import PostMessage from "../models/Listing.js";


export const getRecommendedPosts = async (req, res) => {
    try{    console.log(req.query.city[0])
            if(req.query.state === "" && req.query.city === ""){
                
                const PostMessages = await PostMessage.aggregate([{$sample: {size:20}}])
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
            else if(req.query.city === ""){
                
                const PostMessages = await PostMessage.aggregate([{$match: { $or: [
                    {state:req.query.state[1]},
                    {state:req.query.state[0]},
                    {state:req.query.state[2]}]
                    
                }},{$sample:{size:25}}]);
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
            else{
                console.log(req.query.city[1])
                const PostMessages = await PostMessage.aggregate([{$match: { $or: [
                    {city:req.query.city[1]},
                    {city:req.query.city[0]},
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

export const getPosts = async (req, res) => {
    console.log("hello1");
    try{
        console.log("hello");
        const PostMessages = await PostMessage.find({key: "Florida"});
        console.log(PostMessages);
        res.status(200).json(PostMessages);

    }
    catch(error){
        
        res.status(404).json({message: error.message});
    }
}