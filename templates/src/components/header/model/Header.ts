export interface Header {
    title: string;
    menus: Menu[];
}

export interface Menu {
    title: string;
    path: string;
    subMenu?: Menu[] | null;
}

export default Header
