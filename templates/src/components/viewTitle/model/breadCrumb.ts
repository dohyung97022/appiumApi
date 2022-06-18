class BreadCrumb {
    title: string
    path: string
    isLink: boolean

    constructor(title: string, path: string, isLink: boolean) {
    this.title = title
    this.path = path
    this.isLink = isLink
  }
}

export default BreadCrumb
