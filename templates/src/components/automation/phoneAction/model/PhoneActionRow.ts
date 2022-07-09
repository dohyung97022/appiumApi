import PhoneActionAssociation from "@/model/PhoneActionAssociation";

export class PhoneActionRow {
    id: number;
    name: string;
    phoneActionAssociation: PhoneActionAssociation;

    constructor(id: number, phoneActionAssociation: PhoneActionAssociation) {
        this.id = id;
        this.phoneActionAssociation = phoneActionAssociation;
        this.name = phoneActionAssociation.action.name;
    }
}

export default PhoneActionRow
