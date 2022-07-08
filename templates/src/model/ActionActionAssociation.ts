import Action from "@/model/Action";

export default class ActionActionAssociation {
    action_action_association_seq: number | null;
    parent_action_seq: number | null;
    child_action_seq: number | null;
    association_order: number;
    child_action: Action;

    constructor(parent_action: Action, child_action: Action, association_order: number) {
        this.action_action_association_seq = null;
        this.parent_action_seq = parent_action.action_seq
        this.child_action_seq = child_action.action_seq
        this.child_action = child_action
        this.association_order = association_order
    }
}
