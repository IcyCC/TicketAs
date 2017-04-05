/**
 * Created by Su chang on 2017/3/30.
 */
/**
 * Created by Su chang on 2017/2/28.
 */
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import api from '../middlewares/api';
import  rootReducer from "../reducer/index"

//
// {
// user:{username:"",id},
//  essays:[{title:"",body....},],
// nav_list:[],
// current:"",
// writer:{title:"",body:"",kind_id:"",options:[]}
// discuss:{
//      post:[],
// }
// }

var initalState = {

};

export const store = createStore (rootReducer,initalState,compose(
    applyMiddleware(thunk),
    applyMiddleware(api)
));



