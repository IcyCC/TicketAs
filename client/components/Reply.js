/**
 * Created by Su chang on 2017/3/27.
 */
/**
 * Created by Su chang on 2017/3/20.
 */
import { Form, Icon, Input, Button, Checkbox } from 'antd';
import {hashHistory}  from 'react-router';
import React ,{Component}from "react"

export class Reply extends React.Component {
    constructor(props){
    super(props);
    this.state={
        isShow:false,
        body:""
    }
 }

 onSubmit(e){
        e.preventDefault();
            $.ajax({
        url:"/discuss/comments",
        type:"post",
        data:{
            post_id:this.props.post_id,
            body:this.state.body
        }
    }).done(function(resp){
        if(resp.status == "success")
        {
            alert("success");
            this.setState({body:""});
        }
        if(resp.status == "fail")
        {
            alert(resp.reason);
        }
    }.bind(this))
     this.props.handleRefresh();
 }

 onChange(e){
     this.setState({body:e.target.value})
 }


  render() {
      var m_comment = this.props.comments.map(function(item,index){
            return <div key={item.id+"reply"}><span style={{color:"#1E90FF"}}>{item.username}</span>:<h4>{item.body}</h4>
                    <div><span>{item.timestamp}</span></div></div>
        });
      return this.state.isShow?<div>
              <span onClick={(e)=>{this.setState({isShow:false})}} >收起回复</span>
          <div className="comments" >
              {m_comment}
          </div>
          <form className="form-control" onSubmit={this.onSubmit.bind(this)}>
          <input type="text" placeholder="input you reply...." className="form-inline"
                 onChange={this.onChange.bind(this)}/>
          <input type="submit" className="btn-primary" />
          </form>
          </div>:<a onClick={(e)=>{this.setState({isShow:true})}} >展开回复</a>
  }
}


/**
 * Created by Su chang on 2017/3/27.
 */
