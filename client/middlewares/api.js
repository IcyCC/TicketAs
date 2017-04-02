/**
 * Created by Su chang on 2017/3/4.
 */
import fetch from 'isomorphic-fetch';
import merge from 'lodash.merge';

export default ({dispatch,getState})=>{
        return next => action =>{
            //????

            const { type,api,playload,method,...rest } = action;

            if(!api)
            {
                return next(action);
            }
            console.log("middleware",method);
            next({...rest,type,status:'FETCHING'});


            return $.ajax({
                    type:method,
                    url:api,
                    data:playload,
                    withCredentials: true
            }).done((resp)=>{
                if(resp.status !="success")
                {
                    next({...rest,type,api,status:"ERROR"})
                }
                else
                {
                    next(merge({},{ ...rest, type, api, status: 'SUCCESS', playload: resp }))
                }
            })
        }
    }