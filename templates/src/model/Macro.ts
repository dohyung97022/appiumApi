export default class Macro {
    macro_seq: number | null
    action_seq: number
    name: string
    element: string
    element_type: string
    macro_type: string
    macro_order: number
    macro_index: number
    min_wait_sec: number
    max_wait_sec: number

    constructor(action_seq: number) {
        this.macro_seq = null;
        this.action_seq = action_seq
        this.name = '';
        this.element = '';
        this.element_type = 'ID';
        this.macro_type = 'CLICK';
        this.macro_order = 0;
        this.macro_index = 0;
        this.min_wait_sec = 0;
        this.max_wait_sec = 0;
    }
}
