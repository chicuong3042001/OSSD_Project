class YoutubeChannel {
    _id;
    _index;
    _name;
    _channelId;
    _playlistId;
    _thumbnail;
    _banner;
    _viewCount;
    _subscriberCount;
    _publishedAt;

    constructor() {
        this._id = null;
        this._index = null;
        this._name = null;
        this._channelId = null;
        this._playlistId = null;
        this._thumbnail = null;
        this._banner = null;
        this._viewCount = null;
        this._subscriberCount = null;
        this._publishedAt = null;
    }

    // Getter và setter cho _id
    get id() {
        return this._id;
    }

    set id(value) {
        this._id = value;
    }

    // Tương tự cho các thuộc tính còn lại
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

    get channelId() {
        return this._channelId;
    }

    set channelId(value) {
        this._channelId = value;
    }

    get playlistId() {
        return this._playlistId;
    }

    set playlistId(value) {
        this._playlistId = value;
    }

    get thumbnail() {
        return this._thumbnail;
    }

    set thumbnail(value) {
        this._thumbnail = value;
    }

    get banner() {
        return this._banner;
    }

    set banner(value) {
        this._banner = value;
    }

    get viewCount() {
        return this._viewCount;
    }

    set viewCount(value) {
        this._viewCount = value;
    }

    get subscriberCount() {
        return this._subscriberCount;
    }

    set subscriberCount(value) {
        this._subscriberCount = value;
    }

    get publishedAt() {
        return this._publishedAt;
    }

    set publishedAt(value) {
        this._publishedAt = value;
    }
}