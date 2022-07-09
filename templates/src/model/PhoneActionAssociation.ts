import Action from "@/model/Action";
import Phone from "@/model/Phone";

export default class PhoneActionAssociation {
    phone_action_association_seq: number | null;
    udid: number | null;
    action_seq: number | null;
    loop: number;
    loop_type: string;
    phone: Phone;
    action: Action;

    constructor(phoneActionAssociation: Partial<PhoneActionAssociation> = {}) {
        this.phone_action_association_seq = phoneActionAssociation.phone_action_association_seq ?? null;
        this.udid = phoneActionAssociation.udid ?? null;
        this.action_seq = phoneActionAssociation.phone_action_association_seq ?? null;
        this.loop = phoneActionAssociation.loop ?? 0;
        this.loop_type = phoneActionAssociation.loop_type ?? 'DAILY'
        this.phone = phoneActionAssociation.phone ?? new Phone();
        this.action = phoneActionAssociation.action ?? new Action();
    }
}
