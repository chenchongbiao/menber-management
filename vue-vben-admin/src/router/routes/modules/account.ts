import type { AppRouteModule } from '/@/router/types';

import { LAYOUT } from '/@/router/constant';

const dashboard: AppRouteModule = {
  path: '/account',
  name: 'Account',
  component: LAYOUT,
  redirect: '/account/index',
  meta: {
    icon: 'simple-icons:about-dot-me',
    title: '新账号管理',
  },
  children: [
    {
      path: 'index',
      name: 'AccountIndex',
      component: () => import('/@/views/account/index.vue'),
      meta: {
        title: '账号管理',
        icon: 'simple-icons:about-dot-me',
      },
    },
  ],
};

export default dashboard;
