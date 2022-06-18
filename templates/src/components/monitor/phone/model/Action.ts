export interface Action {
    action_seq: bigint
    name: string
    children: Action[]
}

export default Action
