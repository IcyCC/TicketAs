/**
 * Created by Su chang on 2017/3/31.
 */
import {LOGIN_USER,LOGOUT_USER,REGISTER_USER,FETCH_USER} from "../actions/index"
import _ from 'lodash';

var initalState = {
  isFetching:true,
    user:{},
    is_login:false
};

export default function reducer(state = initalState, action = {}) {
    console.log("essays reducer",action)
  switch (action.type) {
    case LOGIN_USER:
      if (action.status === 'FETCHING') {

          return {isFetching:true,
          user:{},is_login:false}
      }
      if (action.status === 'SUCCESS') {
          console.log(action.playload)

        return {
          isFetching:false,
            user:action.playload.user,
            is_login:true
        }
      }
      break;
      case LOGOUT_USER:
          if (action.status === 'FETCHING') {

          return {isFetching:true,
          user:{},is_login:false}
      }
      if (action.status === 'SUCCESS') {
          console.log(action.playload)

        return {
          isFetching:false,
            user:{},
            is_login:false
        }
      }
          break;
      case REGISTER_USER:
          if (action.status === 'FETCHING') {

          return {isFetching:true,
          user:{},is_login:false}
      }
      if (action.status === 'SUCCESS') {
          console.log(action.playload)

        return {
          isFetching:false,
            user:{},
            is_login:false
        }
      }
          break;
      case FETCH_USER:
          if (action.status === 'FETCHING') {

          return {isFetching:true,
          user:{},is_login:false}
      }
      if (action.status === 'SUCCESS') {
          console.log(action.playload);
        if(action.playload.status == 'success')
        {
                    return {
          isFetching:false,
            user:action.playload.user,
            is_login:true
        }
        }
        else{
                    return {
          isFetching:false,
            user:{},
            is_login:false
           }
        }

      }
          break;
    default:
      return state;
  }
}/**
 * Created by Su chang on 2017/4/2.
 */
/**
 * Created by Su chang on 2017/4/2.
 */
