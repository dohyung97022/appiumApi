import {RouteRecordRaw} from "vue-router";

export interface HeaderRouteRecord {
    routeRecord: RouteRecordRaw;
    isDisplayed: boolean;
    isView: boolean;
}

export default HeaderRouteRecord
