import * as api from '../api'

export const getPosts = (filters) => async (dispatch) => {
    try{
        const { data } = await api.fetchPosts(filters);
        dispatch({type: 'FETCH_ALL', payload: data});
    }
    catch(error){
        console.log(error.message);
    }
    


}

export const getResults = (filters) => async (dispatch) => {
    console.log("Howdy");
    try{
        const { data } = await api.fetchResults(filters);
        dispatch({type: 'FETCH_ALL', payload: data});
    }
    catch(error){
        console.log("hello2");
        console.log(error.message);
    }
    


}