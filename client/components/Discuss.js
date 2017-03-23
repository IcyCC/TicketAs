
import React ,{Component}from "react"
import { Card, Col, Row } from 'antd';
import {WriterFrom} from './Writer'
import SourceCard from "./SourceCard"

export default class Discuss extends Component {
    constructor(props) {
        super(props);
        this.state = {
            posts: [],
            writer: {
                title: "",
                body: "",
                kind_id: "",
                options: []
            }
        }
    }

    onTitleChange(e) {
        this.setState({
            writer: Object.assign({}, this.state.writer, {title: e.target.value})
        });
    }

    onContentChange(e) {
        this.setState({
            writer: Object.assign({}, this.state.writer, {body: e})
        });
    }

    onSelectChange(value) {
        this.setState({
            writer: Object.assign({}, this.state.writer, {kind_id: value})
        });
    }

    componentWillMount() {
        this.getPosts();
    }

    getPosts() {
        $.ajax({
            url: "/discuss/post",
            type: "get",
            withCredentials: true
        }).done(function (resp) {
            if (resp.status == "success") {
                this.setState({posts: resp.posts})
            }
        }.bind(this))
    }

    handleSubmit(e) {
        e.preventDefault();
        $.ajax({
            url: "/discuss/post",
            type: "post",
            withCredentials: true,
            data: {
                tittle: this.state.writer.title,
                body: this.state.writer.body
            },

        }).done(function (resp) {
            alert('success');
            this.getPosts();
        }.bind(this))

    }

    render() {
        let posts = this.state.posts.map(function (item, index) {
            return <Col span={14} offset={5} key={"post" + item.id}><SourceCard card={item} /></Col>
        });
        console.log("discuss",posts);
        return this.props.is_login ?
            <div>
                <Col span={14} offset={5}><WriterFrom writer={this.state.writer} onTitleChange={this.onTitleChange.bind(this)}
                            onContentChange={this.onContentChange.bind(this)}
                            onSelectChange={this.onSelectChange.bind(this)}
                            handleSubmit={this.handleSubmit.bind(this)}/></Col>
                <div>{posts}</div>
            </div>:<div><h1>请先登陆......</h1><div>{posts}</div></div>
    }
}
/**
 * Created by Su chang on 2017/3/20.
 */
