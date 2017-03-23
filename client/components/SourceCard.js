/**
 * Created by Su chang on 2017/3/20.
 */
import React ,{Component}from "react"
import { Card } from 'antd';
import {Link} from 'react-router'

export default function({card}){

     if(typeof (card.user)== "undefined" )
     {
         return <Card title={card.tittle}   style={{height:200 }}>
         <p><small>{card.timestamp}</small></p>
         <p style={{color:"#606060"}}>{card.body}</p>
         </Card>
     }
     else{
              return  <Card title={card.tittle}   style={{height:200 }}>
         <h3 style={{color:"#1E90FF"}}>{card.user.username} :</h3>
         <p><small>{card.timestamp}</small></p>
         <p style={{color:"#606060"}}>{card.body}</p>
         </Card>
     }

}

/**
 * Created by Su chang on 2017/3/20.
 */
