/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VCModelEnum } from './VCModelEnum'
export type VCImagePost = {
  /**
   * The ML model for classifying vehicles
   *
   * * `EfficientNetB1` - EFFNETB1
   * * `YOLOv8s-cls` - YOLOV8SCLS
   */
  model?: VCModelEnum
  /**
   * The image file to be uploaded
   */
  image: string
}
