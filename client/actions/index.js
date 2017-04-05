/**
 * Created by Su chang on 2017/3/30.
 */
export const FETCH_NAV = "FETCH_NAV"
export const fetch_nav =()=>{
    return {
        type:"FETCH_NAV",
        api:"/kind",
        method:'get',
        playload:{}
    }
}


export const FETCH_ESSAY = "FETCH_ESSAY"
export const fetch_essay =(id)=>{
    return {
        type:"FETCH_ESSAY",
        api:"/essay",
        method:'get',
        playload:{id:id}
    }
}


export const PUT_ESSAY= "PUT_ESSAY"
export const put_essay =(title,body,kind_id)=>{
    return {
        type:"PUT_ESSAY",
        api:"/essay",
        method:'post',
        playload:{tittle:title,
                body:body,
                kind:kind_id
            }
    }
}

export const FETCH_POST = "FETCH_POST"
export const fetch_post =()=>{
    return {
        type:"FETCH_POST",
        api:"/discuss/post",
        method:'get',
        playload:{}
    }
}

export const PUT_POST = "FETCH_POST"
export const put_post =(title,body)=>{
    return {
        type:"PUT_POST",
        api:"/discuss/post",
        method:'post',
        playload:{
            tittle: title,
                body: body
        }
    }
}


export const PUT_COMMENTS = "PUT_COMMENTS"
export const put_comments =(post_id,body)=>{
    return {
        type:"PUT_COMMENTS",
        api:"/discuss/comments",
        method:'post',
        playload:{
            post_id:post_id,
            body:body
        }
    }
}


export const LOGIN_USER = "LOGIN_USER"
export const login_user =(data)=>{
    return {
        type:"LOGIN_USER",
        api:"/auth/login",
        method:'post',
        playload:data
    }
}

export const FETCH_USER = "FETCH_USER"
export const fetch_user =()=>{
    return {
        type:"FETCH_USER",
        api:"auth/current",
        method:'get',
        playload:{}
    }
}


export const LOGOUT_USER = "LOGOUT_USER"
export const logout_user =()=>{
    return {
        type:"LOGOUT_USER",
        api:"/auth/logout",
        method:'get',
        playload:{}
    }
}

export const REGISTER_USER = "REGISTER_USER"
export const register_user =(data)=>{
    return {
        type:"REGISTER_USER",
        api:"/auth/users",
        method:'post',
        playload:data
    }
}

