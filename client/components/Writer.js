/**
 * Created by Su chang on 2017/3/20.
 */
import React ,{Component}from "react"
import { Menu, Icon } from 'antd';
var ReactDOM = require('react-dom');
import {Link} from 'react-router'
import { Alert } from 'antd';
import {MarkdownEditor} from 'react-markdown-editor';
import { Select, Form,Input, Button,Checkbox,Col} from 'antd';
const Option = Select.Option;
const FormItem = Form.Item;

 class Writer extends Component{
 constructor(props){
    super(props);

    this.state={
        options:[],
    }
 }

 componentWillMount() {

  }




 render(){

     var opts = this.props.writer.options.map((item)=>{
         return <Option value={String(item.id)}>{item.name}</Option>
     });

      const { getFieldDecorator } = this.props.form;

      console.log(this.props.writer);
     return  <div><Form  onSubmit={this.props.handleSubmit}>
         <h1>写作区</h1>
         <FormItem>{getFieldDecorator('title', {
            rules: [{ required: true, message: 'Please input your title!' }],
          })(
            <Input  placeholder="title" onChange={this.props.onTitleChange.bind(this)}/>
          )}</FormItem>
         <FormItem>
         <MarkdownEditor initialContent="Test" iconsSet="font-awesome" onContentChange={this.props.onContentChange.bind(this)}/>
         <Select defaultValue="none" onChange={this.props.onSelectChange.bind(this)}>{opts}</Select>
             <Col span={4} offset={2}><Button type="primary" htmlType="submit">提交</Button></Col> <Col span={4} offset={2}><Button type="primary" ><Link to="/">返回</Link></Button></Col></FormItem>

     </Form></div>

 }
}
export const WriterFrom = Form.create()(Writer);