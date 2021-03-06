from shmitter.base.permissions import ShmitterPermission
from shmitter.base.permissions import AllowAny, IsAuthenticated, IsObjectOwner


class TweetPermission(ShmitterPermission):
    create_perms = IsAuthenticated()
    destroy_perms = IsObjectOwner()
    update_perms = IsObjectOwner()
    partial_update_perms = IsObjectOwner()

    like_perms = IsAuthenticated()
    unlike_perms = IsAuthenticated()
    fans_perms = AllowAny()
    retweet_perms = IsAuthenticated()
    undo_retweet_perms = IsAuthenticated()
