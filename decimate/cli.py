import argparse
import decimate as m


def main():
    ap = argparse.ArgumentParser(description="网格简化与误差控制")
        ap.add_argument("--target", type=int, required=True)
        ap.add_argument("--out", required=True)
    a = ap.parse_args()
        print("TODO")


if __name__ == "__main__":
    main()
