
import { combineReducers } from 'redux';
import essay from './essay';
import kind from './kind';
import user from "./user"

const rootReducer = combineReducers({
    essay,kind,user
});

export default rootReducer;
