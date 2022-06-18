import Macro from "@/components/automation/action/model/Macro";
import ActionNode from "@/components/automation/action/model/ActionNode";

export default class Action {
    action_seq: number | null;
    name: string;
    macros: Macro[];
    child_actions: Action[];

    constructor(name: string) {
        this.action_seq = null;
        this.name = name;
        this.macros = [];
        this.child_actions = [];
    }

    static ofActionNode(actionNode: ActionNode): Action {
        actionNode.action.child_actions = actionNode.$children.map(childAction => this.ofActionNode(childAction));
        actionNode.action.name = actionNode.text
        return actionNode.action
    }
}
