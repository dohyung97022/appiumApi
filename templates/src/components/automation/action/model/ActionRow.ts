import Action from "@/model/Action";

export class ActionRow {
    id: number;
    name: string;
    action: Action;

    constructor(action: Action, id: number) {
        this.id = id
        this.name = action.name
        this.action = action
    }
}

export default ActionRow
