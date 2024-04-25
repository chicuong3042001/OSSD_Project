class Fanpage {
    _id; _index; _name; _likes; _fanpageId; _fanpageIdDelegate; _avatar; _banner; _checkins; _platform;
    constructor() {
        this._id = 0;
        this._index = 0;
        this._name = '';
        this._likes = 0;
        this._fanpageId = '';
        this._fanpageIdDelegate = '';
        this._avatar = '';
        this._banner = '';
        this._checkins = 0;
        this._platform = 'FANPAGE'
    }

    get platform() {
        return this._platform;
    }

    set platform(value) {
        this._platform = value;
    }

    get id() {
        return this._id;
    }
    set id(value) {
        this._id = value;
    }
    get index() {
        return this._index;
    }
    set index(value) {
        this._index = value;
    }
    get name() {
        return this._name;
    }
    set name(value) {
        this._name = value;
    }
    get likes() {
        return this._likes;
    }
    set likes(value) {
        this._likes = value;
    }


    get checkins() {
        return this._checkins;
    }

    set checkins(value) {
        this._checkins = value;
    }

    get fanpageId() {
        return this._fanpageId;
    }
    set fanpageId(value) {
        this._fanpageId = value;
    }
    get fanpageIdDelegate() {
        return this._fanpageIdDelegate;
    }
    set fanpageIdDelegate(value) {
        this._fanpageIdDelegate = value;
    }

    get avatar() {
        return this._avatar;
    }
    set avatar(value) {
        this._avatar = value;
    }


    get banner() {
        return this._banner;
    }

    set banner(value) {
        this._banner = value;
    }
}
