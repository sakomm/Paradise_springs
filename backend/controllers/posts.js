import PostMessage from "../models/Listing.js";
import Safety from "../models/Safety.js"

export const getRecommendedPosts = async (req, res) => {
    try{    
            
            
            

            if(req.query.key !==undefined){
                //console.log("hi-one");
                //console.log(req.query.key)
               const Rating = await Safety.find({key:req.query.key})
               //console.log(Rating);
                res.status(200).json(Rating);
            }

            else if(req.query.state === undefined && req.query.city === undefined){
                console.log("hi-two")
                const PostMessages = await PostMessage.aggregate([{$sample: {size:20}}])
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
            else if(req.query.state && req.query.state[0].length>1){
                console.log(true);
                 const PostMessages = await PostMessage.aggregate([{$match: { $or: [
                    {state:req.query.state[0]},
                    {state:req.query.state[1]},
                    {state:req.query.state[2]}]
                    
                }},{$sample:{size:25}}]);
                console.log(PostMessages);
                res.status(200).json(PostMessages);
            }     
            else if(req.query.city && req.query.city[0].length>1){
                console.log(true);
                 const PostMessages = await PostMessage.aggregate([{$match: { $or: [
                    {city:req.query.city[0]},
                    {city:req.query.city[1]},
                    {city:req.query.city[2]}]
                    
                }},{$sample:{size:25}}]);
                console.log(PostMessages);
                res.status(200).json(PostMessages);
            }       
            else{
                var arr =[];
                console.log("hi-four")
                let query ={};
                if(req.query.state && req.query.state!='undefined'){
                    query.state = req.query.state;
                }
                if(req.query.city &&req.query.city!='undefined'){
                    console.log(req.query.city)
                    query.city = req.query.city;
                }
                if(req.query.rental_amenities && req.query.rental_amenities!== 'undefined'){
                    
                    
                    arr.push(req.query.rental_amenities);
                    query.rental_amenities = req.query.rental_amenities;
                }
                if(req.query.check_out&& req.query.check_out!='undefined'){
                    query.Check_out = {$gte:req.query.check_out};
                }
                if(req.query.check_in&& req.query.check_in!='undefined'){
                    query.Check_in = {$lte:req.query.check_in};
                }
               
                if(req.query.price&& req.query.price!='undefined'){
                    query.rental_price= {$lte:req.query.price};
                }
                if(req.query.beds&& req.query.beds!='undefined'){
                    arr.push(req.query.beds);
                    query.rental_amenities = {$all: arr};
                }
                if(req.query.wifi&& req.query.wifi!='undefined'){
                    arr.push(req.query.wifi);
                    query.rental_amenities = {$all: arr};
                }
                if(req.query.kitchen&& req.query.kitchen!='undefined'){
                    arr.push(req.query.kitchen);
                    query.rental_amenities = {$all: arr};
                }

                console.log(query)
                const PostMessages = await PostMessage.aggregate([
                    {$match: 
                        query
                    },{$sample: {size:30}}]);
                console.log(PostMessages);
                res.status(200).json(PostMessages);
            }

            /*
            else{
             
                const PostMessages = await PostMessage.aggregate([{$match: { $or: [
                    {city:req.query.city[0]},
                    {city:req.query.city[1]},
                    {city:req.query.city[2]}]
                    
                }},{$sample:{size:25}}]);
                //console.log(PostMessages);
                res.status(200).json(PostMessages);
            }
       
        */

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