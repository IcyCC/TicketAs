/**
 * Created by Su chang on 2017/3/20.
 */
import { Form, Icon, Input, Button, Checkbox } from 'antd';
const FormItem = Form.Item;
import {hashHistory}  from 'react-router';

class NormalLoginForm extends React.Component {
    constructor(props){
    super(props);

    this.state={
        username:"",
        password:"",
        remeber_me:false
    }
 }

 handleUsernameChang(e){
     this.setState({username:e.target.value})
 }
 handlePasswordChange(e){
     this.setState({password:e.target.value})
 }
 handleRemeberChange(e){
     console.log(e);
     this.setState({remeber_me:e.target.checked})
 }


  handleSubmit = (e) => {
    e.preventDefault();
    $.ajax({
        url:"/auth/login",
        type:"post",
        data:{
            username:this.state.username,
            password:this.state.password,
            remeber_me:this.state.remeber_me
        }
    }).done(function(resp){
        if(resp.status == "success")
        {
            alert("success")
            hashHistory.push( '/');
        }
        if(resp.status == "fail")
        {
            alert(resp.reason);
        }
    }.bind(this))

  }
  render() {
     console.log(this.state);
    const { getFieldDecorator } = this.props.form;
    return (
      <Form onSubmit={this.handleSubmit.bind(this)} className="login-form">
        <FormItem>
          {getFieldDecorator('userName', {
            rules: [{ required: true, message: 'Please input your username!' }],
          })(
            <Input prefix={<Icon type="user" style={{ fontSize: 13 }} />} placeholder="Username" onChange={this.handleUsernameChang.bind(this)}/>
          )}
        </FormItem>
        <FormItem>
          {getFieldDecorator('password', {
            rules: [{ required: true, message: 'Please input your Password!' }],
          })(
            <Input prefix={<Icon type="lock" style={{ fontSize: 13 }} />} type="password" placeholder="Password" onChange={this.handlePasswordChange.bind(this)} />
          )}
        </FormItem>
        <FormItem>
          {getFieldDecorator('remember', {
            valuePropName: 'checked',
            initialValue: true,
          })(
            <Checkbox onChange={this.handleRemeberChange.bind(this)}>Remember me</Checkbox>
          )}
          <Button type="primary" htmlType="submit" className="login-form-button">
            Log in
          </Button>
        </FormItem>
      </Form>
    );
  }
}

export const Login = Form.create()(NormalLoginForm);

