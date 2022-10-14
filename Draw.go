package main

import (
	"image"
	"image/color"
	"log"

	"github.com/fogleman/gg"
)

func DrawBKGWithCustomOpacity(imgPath string, percentage float64) image.Image {
	img, err := gg.LoadImage(imgPath)
	if err != nil {
		log.Print(err)
		return nil
	}

	bounds := img.Bounds()
	dx := bounds.Dx()
	dy := bounds.Dy()
	newRGBA := image.NewRGBA64(bounds)

	for x := 0; x < dx; x++ {
		for y := 0; y < dy; y++ {
			colorRGB := img.At(x, y)
			r, g, b, a := colorRGB.RGBA()
			opacity := uint16(float64(a) * percentage)

			newRGBA.SetRGBA64(x, y, color.RGBA64{
				R: uint16(r),
				G: uint16(g),
				B: uint16(b),
				A: opacity,
			})
		}
	}

	return newRGBA
}

func main() {
	bkg := DrawBKGWithCustomOpacity("./Source/BKG.png", 0.5)

	dc := gg.NewContext(bkg.Bounds().Max.X, bkg.Bounds().Max.Y)
	dc.SetRGB(1, 1, 1)
	dc.Clear()
	dc.DrawImage(bkg, 0, 0)

	dc.SavePNG("./out.png")
}
