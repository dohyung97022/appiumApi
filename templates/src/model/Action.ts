import Macro from "@/model/Macro";
import ActionNode from "@/components/automation/action/model/ActionNode";
import ActionActionAssociation from "@/model/ActionActionAssociation";

export default class Action {
    action_seq: number | null;
    name: string;
    macros: Macro[];
    child_action_associations: ActionActionAssociation[];
    is_root: boolean;

    constructor(action: Partial<Action> = {}) {
        this.action_seq = action.action_seq ?? null;
        this.name = action.name ?? '';
        this.macros = action.macros ?? [];
        this.child_action_associations = action.child_action_associations ?? [];
        this.is_root = action.is_root ?? false;
    }

    static ofActionNode(actionNode: ActionNode): Action {
        let i = 0;
        actionNode.action.child_action_associations = actionNode.$children.map(
            childAction => new ActionActionAssociation(actionNode.action, this.ofActionNode(childAction), i++));
        actionNode.action.name = actionNode.text
        return actionNode.action
    }
}
