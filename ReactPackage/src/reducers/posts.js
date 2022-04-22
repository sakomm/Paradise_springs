export default (posts = [], action) => {
    if(action.type == 'FETCH_ALL'){
        return action.payload;
    }
    else if(action.type == 'CREATE'){
        return posts;
    }
    else{
        return posts;
    }
    
}