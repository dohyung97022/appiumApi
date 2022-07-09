import PhoneActionAssociation from "@/model/PhoneActionAssociation";

export default class Phone {
    udid: string
    model: string
    action_associations: PhoneActionAssociation[]

    constructor(phone: Partial<Phone> = {}) {
        this.udid = phone.udid ?? '';
        this.model = phone.model ?? '';
        this.action_associations = phone.action_associations ?? [];
    }
}
