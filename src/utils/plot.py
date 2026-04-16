def set_default_axis_style(plt, label_size=20, pad=8):
    plt.tick_params(axis="both", which="major", labelsize=label_size, pad=pad)
    plt.tick_params(axis="both", which="minor", labelsize=label_size, pad=pad)
