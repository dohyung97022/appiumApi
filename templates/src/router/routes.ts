import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { Header, Menu } from "@/components/header/model/Header";
import HeaderRouteRecord from "@/router/model/HeaderRouteRecord";
import homeView from "@/views/HomeView.vue";

const headerRoutes: Array<HeaderRouteRecord> = [
  {
    routeRecord: {
      path: '/',
      name: 'appiumApi',
      component: HomeView
    },
    isDisplayed: true,
    isView: true

  },
  {
    routeRecord: {
      path: '/monitor',
      name: 'monitor',
      component: HomeView
    },
    isDisplayed: true,
    isView: false
  },
  {
    routeRecord: {
      path: '/monitor/phones',
      name: 'phones',
      component: () => import('../views/monitor/MonitorPhonesView.vue')
    },
    isDisplayed: true,
    isView: true
  },
  {
    routeRecord: {
      path: '/automation',
      name: 'automation',
      component: homeView
    },
    isDisplayed: true,
    isView: false
  },
  {
    routeRecord: {
      path: '/automation/phoneAction',
      name: 'phoneAction',
      component: () => import('../views/automation/AutomationPhoneActionView.vue')
    },
    isDisplayed: false,
    isView: true
  },
  {
    routeRecord: {
      path: '/automation/action',
      name: 'action',
      component: () => import('../views/automation/AutomationActionView.vue')
    },
    isDisplayed: false,
    isView: true
  },
  {
    routeRecord: {
      path: '/automation/agentJob',
      name: 'agentJob',
      component: () => import('../views/automation/AutomationAgentJobView.vue')
    },
    isDisplayed: true,
    isView: true
  }
]

function headerRoutesToHeader(): Header {

  // 메뉴 객체
  const menu: Header = {
    title: '',
    menus: []
  };

  for (const route of headerRoutes) {

    // 표시 여부 확인
    if (!route.isDisplayed) {
      continue
    }

    // 홈 추가
    if (route.routeRecord.path == '/') {
      menu.title = <string>headerRoutes[0].routeRecord.name
      continue
    }

    // / 의 개수를 확인
    let slash_amount = 0
    const slash_match = route.routeRecord.path.match(/\//g)
    if (slash_match != null) {
      slash_amount = slash_match.length
    }

    // 하위 메뉴
    const sub_menu: Menu = {
      title: <string>route.routeRecord.name,
      path : route.routeRecord.path,
      subMenu : []
    };

    // 1 depth
    if (slash_amount == 1) {
      // 추가
      menu.menus.push(sub_menu)
    }

    // 2 depth
    if (slash_amount == 2) {
      // 마지막으로 추가된 1 depth 안에 추가
      menu.menus[menu.menus.length - 1].subMenu?.push(sub_menu)
    }
  }

  return menu
}

function headerRoutesToRoutes(): RouteRecordRaw[] {
  return headerRoutes.map((route) => {return route.routeRecord})
}

export function pathExists(path: string): boolean {
  let exists = false
  headerRoutes.forEach(function (headerRoute) {
    if (headerRoute.routeRecord.path === path && headerRoute.isView) {
      exists = true
    }
  })
  return exists
}

export const header: Header = headerRoutesToHeader()

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: headerRoutesToRoutes()
})

export default router
