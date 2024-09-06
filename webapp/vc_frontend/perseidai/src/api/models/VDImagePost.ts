/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VDModelEnum } from './VDModelEnum'
export type VDImagePost = {
  /**
   * The ML model for detecting vehicles
   *
   * * `YOLOv5s` - YOLOV5S
   * * `YOLOv8s` - YOLOV8S
   */
  model?: VDModelEnum
  /**
   * The image file to be uploaded
   */
  image: string
}
