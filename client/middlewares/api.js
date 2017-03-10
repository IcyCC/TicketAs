/**
 * Created by Su chang on 2017/3/4.
 */
import fetch from 'isomorphic-fetch';
import merge from 'lodash.merge';

export default ({dispatch,getState})=>{
        return next => action =>{
            //????

            const { type,api,request,method = 'GET',...rest } = action;

            if(!api)
            {
                return next(action);
            }
            console.log("middleware");
            next({...rest,type,status:'FETCHING'});



           return fetch(api,{
                method,
                headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',},
              credentials: 'same-origin',
                ...(method == 'POST' || method == 'PUT' || method == 'GET' ?
            { body: request && JSON.stringify(request) } :
            {}),
            }).then(resp=>{
                if(resp.status !== 200 )
                {
                    next({...next,type,api,status:"ERROR"});
                }else{
                    resp.json().then(json=>next(merge({},{ ...rest, type, api, status: 'SUCCESS', resp: json })))
                }
            })
        }
    }