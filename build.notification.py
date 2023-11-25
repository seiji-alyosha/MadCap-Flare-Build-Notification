from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(
    "MadCap Flare",
    "Your build has finished!",
    duration = 20,
    threaded = True,
)